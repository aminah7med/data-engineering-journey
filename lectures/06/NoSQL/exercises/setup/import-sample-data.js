const data = EJSON.parse(cat("lectures/06/NoSQL/exercises/setup/sample-data.json"));
const collections = {
  customers: data.customers,
  orders: data.orders,
  products: data.products
};

for (const name of Object.keys(collections)) {
  const existingCount = db.getCollection(name).countDocuments();
  if (existingCount !== 0) {
    throw new Error(
      `Refusing to import: nosql_learning.${name} contains ${existingCount} documents. ` +
      "Use an empty dedicated practice database or inspect and clean it manually."
    );
  }
}

for (const [name, documents] of Object.entries(collections)) {
  const target = db.getCollection(name);
  if (name === "orders") {
    for (const document of documents) {
      document.order_date = new Date(document.order_date);
    }
  }
  target.insertMany(documents);
  print(`Imported ${documents.length} documents into nosql_learning.${name}`);
}
