# Local gpt-oss Docker

Personal exploration to deploy a Docker image for gpt-oss and other models

Exploration paths:
- [ ] Ollama
- [ ] vLLM
- [ ] Text Generation Inference (TGI)
- [ ] LM Studio
- [ ] Custom API layer

Questions I'd like to answer:
- What is the difference between those?
- What particular use cases do they have?
- Can I abstract the Docker implementation to be independent of those tools?


## Ollama
- Is the CLI mainly used for managing models?
- 
1. [Install Ollama CLI](https://ollama.com/download) to manage models.
2. Download an example model. Let's say `gemma3:4b` (not really important which one ATM)
    ```bash
    ollama pull gemma3:4b
    ```
3. Check it was installed
    ```bash
    ollama list
    ```
1. Create a simple script to interact with the model via the [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md).
2. Run it. Keep in mind that the first interaction will take a while, because Ollama needs to load the model.
