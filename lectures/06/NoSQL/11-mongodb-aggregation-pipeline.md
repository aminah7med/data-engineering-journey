# 11. MongoDB Aggregation Pipeline

> **MongoDB-specific:** an aggregation pipeline passes documents through ordered stages. Each stage transforms, filters, or groups the input.

## Revenue by order status

```javascript
db.orders.aggregate([
  { $match: { status: { $in: ["paid", "shipped"] } } },
  {
    $group: {
      _id: "$status",
      order_count: { $sum: 1 },
      revenue: { $sum: "$total" }
    }
  },
  { $sort: { revenue: -1 } }
]);
```

`$match` filters early; `$group` groups by status and computes counts and totals; `$sort` orders the grouped output. The `_id` in `$group` is the group key, not the source document `_id`.

## Revenue by product

```javascript
db.orders.aggregate([
  { $unwind: "$items" },
  {
    $group: {
      _id: "$items.product_id",
      units_sold: { $sum: "$items.quantity" },
      gross_sales: {
        $sum: { $multiply: ["$items.quantity", "$items.unit_price"] }
      }
    }
  },
  { $sort: { gross_sales: -1 } }
]);
```

`$unwind` emits one pipeline document per item. This changes the row/document granularity: order-level values can be counted multiple times after unwinding, so group at the intended grain.

## Join product names

```javascript
db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "products",
      localField: "items.product_id",
      foreignField: "product_id",
      as: "product"
    }
  },
  { $unwind: "$product" },
  {
    $group: {
      _id: "$product.name",
      units_sold: { $sum: "$items.quantity" }
    }
  }
]);
```

`$lookup` is a left-outer-join-like stage; here the next `$unwind` drops rows without a matching product. If unmatched references need to be monitored, retain empty arrays with `$unwind`'s `preserveNullAndEmptyArrays` option.

## Pipeline discipline

Filter early where semantics permit, project only needed fields, verify the document grain after `$unwind`, and test empty/missing inputs. Aggregation is useful for operational transformations but does not automatically make MongoDB an analytical warehouse.
