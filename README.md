# 🐳 **docker-cleanup**  

**A CLI tool to clean all Docker resources (containers, images, volumes, networks, caches) with a single command.**

---

## 📦 **Installation**

To install docker-cleanup from PyPI, run:

```bash
pip install docker-cleanup
```

Or, if you're installing locally from the source:

```bash
pip install .
```

---

## 🚀 **Usage**

docker-cleanup provides a straightforward way to clean up Docker environments.

### **Interactive Mode (with Confirmation)**  
Run the command and confirm the cleanup manually:  

```bash
docker-cleanup
```

- After running the command, you'll be prompted to confirm the cleanup:  
  ```
  ⚠️ This will delete all Docker data (containers, images, volumes, networks). Are you sure? (yes/no):
  ```
- **Type `yes`** to proceed with the cleanup.  
- **Type `no`** to cancel the operation.

This mode is ideal when you want to review the operation before execution.

### **Non-Interactive Mode (Skip Confirmation)**  
Use the `-y` flag to skip confirmation and immediately perform the cleanup:  

```bash
docker-cleanup -y
```

### 🐳 **Prerequisite: Running Docker Without `sudo`**

Before using **docker-cleanup**, ensure Docker commands can be executed **without requiring `sudo` privileges**.  

If Docker commands like `docker ps` or `docker system prune` require `sudo`, follow the official Docker documentation to configure your user permissions:

👉 [**Post-Installation Steps for Linux**](https://docs.docker.com/engine/install/linux-postinstall/)

---

⚠️ **Important:** Without completing this setup, you’ll need to run `docker-cleanup` with `sudo`, which may not work seamlessly with the tool.  

**Ensure Docker runs without `sudo` for the best experience with docker-cleanup! 🚀**

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

If you encounter any issues, please open an issue on [GitHub](https://github.com/0hye/docker-cleanup).  

Enjoy cleaner Docker environments! 🐳✨

### 🤖 **Acknowledgment**

This project was initially conceptualized and structured with the assistance of **ChatGPT by OpenAI**. ChatGPT provided guidance on designing the CLI tool, structuring the project for packaging, and creating clear documentation.  

While the tool's functionality and final implementation are the result of developer effort, the collaborative brainstorming with ChatGPT played a valuable role in shaping its foundation.  

**Thank you, ChatGPT, for being an insightful assistant! 🚀**  
