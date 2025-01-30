# ⚠️ DEPRECATION NOTICE ⚠️

**This project is no longer maintained.**  

This Telegram bot relied on the **Songwhip API** to retrieve music links, but **Songwhip has been discontinued**. As a result, this bot **no longer functions as intended**.  

### What does this mean?
- There will be **no further updates** or bug fixes.
- The bot **may not work correctly** due to the API shutdown.
- If you are looking for a similar service, consider alternative music link aggregators.

### Alternatives
If you're interested in forking or maintaining a similar project, you may need to find a replacement API for music link aggregation.

Thank you to everyone who used and supported this bot!  

---

# songwhip-telegram-inline
The Unofficial Songwhip Telegram Bot that supports inline conversion and search

## Environment variables:
- `TOKEN`: Bot API token from botfather
- `LOGGING_LEVEL`: logging level (optional), default - `info`

## Deploy

Clone this repository: `git clone https://github.com/Slamaio/songwhip-telegram-inline.git`

### Build a Docker image

```bash
docker build -t project-name:tag .
```

> 💡 Change `project-name:tag` to accommodate the current project.

### Upload the image to the Amazon ECR repository

In the following commands, replace `476299868894` with your AWS account ID and set the region value to the region where you want to create the Amazon ECR repository.

> 💡 In Amazon ECR, if you reassign the image tag to another image, Lambda does not update the image version.


1. Authenticate the Docker CLI to your Amazon ECR registry.

```bash
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 476299868894.dkr.ecr.eu-west-2.amazonaws.com
```

2. Create a repository in Amazon ECR using the `create-repository` command. 

```bash
aws ecr create-repository --repository-name project-name --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
```

3. Tag your image to match your repository name, and deploy the image to Amazon ECR using the `docker push` command.

```bash
docker tag project-name:tag 476299868894.dkr.ecr.eu-west-2.amazonaws.com/project-name:tag
docker push 476299868894.dkr.ecr.eu-west-2.amazonaws.com/project-name:tag
```

### Create and configure API Gateway entrypoint
- Create and configure API Gateway entrypoint;
- Set webhook for your bot: follow the link through your browser or using curl – `https://api.telegram.org/bot{your_bot_api_token}/setWebhook?url={your_api_gateway_url}`
