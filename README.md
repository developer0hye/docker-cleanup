# 🐳 **DockerClean**  

**A CLI tool to clean all Docker resources (containers, images, volumes, networks, caches) with a single command.**

---

## 📦 **Installation**

To install DockerClean from PyPI, run:

```bash
pip install dockerclean
```

Or, if you're installing locally from the source:

```bash
pip install .
```

---

## 🚀 **Usage**

DockerClean provides a straightforward way to clean up Docker environments.

### **Interactive Mode (with Confirmation)**  
Run the command and confirm the cleanup manually:  

```bash
dockerclean
```

### **Non-Interactive Mode (Skip Confirmation)**  
Use the `-y` flag to skip confirmation and immediately perform the cleanup:  

```bash
dockerclean -y
```

---

## ⚠️ **Warning**

- This tool **will delete all Docker containers, images, volumes, networks, and caches**.
- The operation is **irreversible**. Ensure you have backed up any important data before proceeding.

---

## 🛠️ **Features**

- 🗑️ **Full Cleanup:** Removes all containers, images, volumes, and networks.  
- ⚡ **Fast Execution:** Skip confirmation with `-y` for immediate cleanup.  
- 🐍 **Easy Installation:** Installable via `pip`.  

---

## 📝 **Contributing**

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature/your-feature`.  
3. Make your changes and commit: `git commit -am 'Add new feature'`.  
4. Push to the branch: `git push origin feature/your-feature`.  
5. Submit a pull request.  

---

## 📄 **License**

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🤝 **Support**

If you encounter any issues, please open an issue on [GitHub](https://github.com/yourusername/dockerclean).  

Enjoy cleaner Docker environments! 🐳✨

### 🤖 **Acknowledgment**

This project was initially conceptualized and structured with the assistance of **ChatGPT by OpenAI**. ChatGPT provided guidance on designing the CLI tool, structuring the project for packaging, and creating clear documentation.  

While the tool's functionality and final implementation are the result of developer effort, the collaborative brainstorming with ChatGPT played a valuable role in shaping its foundation.  

**Thank you, ChatGPT, for being an insightful assistant! 🚀**  
