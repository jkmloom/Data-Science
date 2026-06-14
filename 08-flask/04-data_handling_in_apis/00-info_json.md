# Understanding JSON in API Data Handling

An **API (Application Programming Interface)** allows two different computer programs to talk to each other. When they share information, they need a common language. **JSON (JavaScript Object Notation)** is that language. It is a lightweight, text-based format used to package and transport data.

---

## 🔄 The Core Workflow: Serialization vs. Deserialization

When data travels across an API, it goes through two major steps:

### 1. Serialization (Sending Data)
A server cannot send a live database object or programming variable over the internet. It must convert that data into a flat string of text first. This process is called **serialization** (or stringifying). 

### 2. Deserialization (Receiving Data)
When the receiving app gets the JSON text string, it cannot use it as raw text. It must turn that text back into a live data object (like a dictionary in Python or an object in JavaScript) that the code can manipulate. This is called **deserialization** (or parsing).

---

## 🚀 JSON in the API Request-Response Cycle

API communication works like a restaurant. You make a **Request** (order food), and the server gives you a **Response** (brings food). JSON is used in both steps.

