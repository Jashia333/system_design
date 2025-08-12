````markdown
# 🗄️ Cache API

A lightweight HTTP-based in-memory cache service that supports adding entries with a time-to-live (TTL), retrieving cache data, and checking cache size.

---

## 📦 Features
- **PUT**: Store multiple keys with associated TTLs (in seconds).
- **GET**: Retrieve all valid cache entries.
- **GET size**: Get the number of active cache entries.
- Automatically **prunes expired entries** before returning data.

---

## 🚀 Running the Server

The API runs on `http://localhost:9000` by default.  
If using Flask:
```bash
python app.py
````

Or inside your app:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
```

---

## 🔌 API Endpoints

### **1️⃣ PUT `/cache`**

Add or update multiple keys with data and TTL.

**Request body format:**

```json
{
  "key1": { "data": "string_value", "ttl": seconds },
  "key2": { "data": "string_value", "ttl": seconds }
}
```

**Example:**

```json
{
  "req1": { "data": "Hello from request 1", "ttl": 25 },
  "req2": { "data": "Hello from request 2", "ttl": 30 },
  "req3": { "data": "Hello from request 3", "ttl": 35 }
}
```

---

### **2️⃣ GET `/cache/show`**

Returns all current cache entries (expired entries are removed before returning).

**Example Response:**

```json
{
  "data": {
    "req1": ["Hello from request 1", 1691752923.12],
    "req2": ["Hello from request 2", 1691752928.45]
  }
}
```

---

### **3️⃣ GET `/cache/size`**

Returns the number of active cache entries.

**Example Response:**

```json
{
  "keys_length": 2
}
```

---

## 📂 Creating the JSON File

Save your data in a file named `body.json`:

```json
{
  "req1": { "data": "Hello from request 1", "ttl": 25 },
  "req2": { "data": "Hello from request 2", "ttl": 30 },
  "req3": { "data": "Hello from request 3", "ttl": 35 }
}
```

---

## 💻 Usage Examples

### **PUT data into cache**

#### **PowerShell (Windows)**

```powershell
Invoke-RestMethod -Uri "http://localhost:9000/cache" `
  -Method Put `
  -ContentType "application/json" `
  -InFile "body.json"
```

#### **curl (Linux/Mac or Windows CMD)**

```bash
curl -X PUT "http://localhost:9000/cache" \
  -H "Content-Type: application/json" \
  --data-binary "@body.json"
```

---

### **GET all cache entries**

#### **PowerShell**

```powershell
Invoke-RestMethod -Uri "http://localhost:9000/cache/show" -Method Get
```

#### **curl**

```bash
curl -X GET "http://localhost:9000/cache/show"
```

---

### **GET cache size**

#### **PowerShell**

```powershell
Invoke-RestMethod -Uri "http://localhost:9000/cache/size" -Method Get
```

#### **curl**

```bash
curl -X GET "http://localhost:9000/cache/size"
```

---

## 📝 Notes

* **TTL** is in seconds. Expired keys are removed before data is returned.
* JSON property names must be in **double quotes**.
* If using PowerShell, prefer `Invoke-RestMethod` to avoid quoting issues with `curl`.

---

## 📜 License

This project is free to use and modify for educational or commercial purposes.

```

---

If you want, I can also **add a “Getting a single key” endpoint section** so your README covers key-based lookups too.  
Do you want me to add that?
```
