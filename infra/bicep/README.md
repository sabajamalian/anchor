# Azure Infrastructure

This directory contains Bicep templates for deploying the Anchor Starter application to Azure.

## Prerequisites

- Azure CLI installed and configured
- Azure subscription
- Appropriate permissions to create resources

## Resources Created

The Bicep template creates the following Azure resources:

1. **App Service Plan** (Linux, Basic tier)
2. **App Service** (Web App for containers)
3. **Azure SQL Server**
4. **Azure SQL Database** (Basic tier)
5. **Storage Account** (for blob storage)
6. **Blob Container** (for file uploads)

## Deployment with Azure Developer CLI (azd)

The easiest way to deploy is using `azd`:

```bash
# Initialize azd (first time only)
azd init

# Login to Azure
azd auth login

# Deploy the infrastructure and application
azd up
```

## Manual Deployment

### 1. Create Resource Group

```bash
az group create --name anchor-rg --location eastus
```

### 2. Deploy Bicep Template

```bash
az deployment group create \
  --resource-group anchor-rg \
  --template-file main.bicep \
  --parameters appName=anchor-starter \
               environmentName=dev \
               sqlAdminLogin=sqladmin \
               sqlAdminPassword='YourSecurePassword123!'
```

### 3. Get Outputs

```bash
az deployment group show \
  --resource-group anchor-rg \
  --name main \
  --query properties.outputs
```

## Parameters

- **appName**: Name of the application (default: `anchor-starter`)
- **location**: Azure region for resources (default: resource group location)
- **environmentName**: Environment (dev/staging/prod)
- **sqlAdminLogin**: SQL Server administrator username
- **sqlAdminPassword**: SQL Server administrator password (secure string)

## Customization

Edit `main.bicep` to customize:
- SKU tiers for App Service and SQL Database
- Storage account type
- Add additional Azure resources (e.g., Application Insights, Key Vault)

## Security Best Practices

1. Store sensitive parameters in Azure Key Vault
2. Use managed identities for Azure resource authentication
3. Enable diagnostic logging and monitoring
4. Configure appropriate firewall rules for SQL Server
5. Use private endpoints for production environments
