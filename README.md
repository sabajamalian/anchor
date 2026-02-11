# ⚓ Anchor Starter

A production-ready starter template for building web applications with Python FastAPI, Azure SQL, Azure Storage, and Docker.

## 🚀 Tech Stack

- **Backend**: FastAPI (Python 3.12)
- **Frontend**: Vanilla HTML/CSS/JavaScript with PicoCSS
- **Database**: Azure SQL Server with SQLAlchemy
- **Storage**: Azure Blob Storage
- **Infrastructure**: Azure App Service + Bicep (IaC)
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Testing**: pytest
- **Code Quality**: Ruff

## 📁 Project Structure

```
anchor/
├── src/
│   ├── backend/
│   │   ├── app/
│   │   │   ├── routers/       # API endpoints organized by resource
│   │   │   ├── models/        # SQLAlchemy models
│   │   │   ├── database/      # Database connection and utilities
│   │   │   ├── config.py      # Application configuration
│   │   │   └── main.py        # FastAPI application entry point
│   │   ├── tests/             # pytest test suite
│   │   └── requirements.txt   # Python dependencies
│   └── frontend/
│       ├── templates/         # HTML templates
│       └── static/
│           ├── css/           # Stylesheets (PicoCSS)
│           └── js/            # Vanilla JavaScript
├── database/
│   └── migrations/            # Raw SQL migration scripts
├── infra/
│   └── bicep/                 # Azure infrastructure as code
├── .github/
│   └── workflows/             # GitHub Actions CI/CD
├── Dockerfile                 # Container configuration
├── docker-compose.yml         # Local development setup
├── azure.yaml                 # Azure Developer CLI config
└── pyproject.toml             # Ruff configuration

```

## 🏃 Quick Start

### Prerequisites

- Python 3.12+
- Docker and Docker Compose
- Azure CLI (for deployment)
- Azure Developer CLI (optional, for `azd up`)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/sabajamalian/anchor.git
   cd anchor
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up
   ```

4. **Access the application**
   - Web UI: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

### Alternative: Run Locally (without Docker)

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r src/backend/requirements.txt
   ```

3. **Run the application**
   ```bash
   cd src/backend
   python -m uvicorn app.main:app --reload
   ```

## 🧪 Testing

Run the test suite:

```bash
pytest src/backend/tests/ -v
```

Run tests with coverage:

```bash
pytest src/backend/tests/ --cov=app --cov-report=html
```

## 🎨 Code Quality

Format code with Ruff:

```bash
ruff format src/backend/app
```

Lint code with Ruff:

```bash
ruff check src/backend/app
```

Fix linting issues automatically:

```bash
ruff check --fix src/backend/app
```

## 🗄️ Database

### Running Migrations

Migrations are raw SQL scripts located in `database/migrations/`.

**Using sqlcmd:**
```bash
sqlcmd -S localhost -d anchor_db -U sa -P 'YourStrong@Passw0rd' -i database/migrations/001_create_items_table.sql
```

**Using Azure Data Studio or SQL Server Management Studio:**
1. Connect to your database
2. Open and execute each migration file in order

### Creating New Migrations

1. Create a new file: `database/migrations/XXX_description.sql`
2. Add migration header and SQL statements
3. Test on development database
4. Execute in production

## ☁️ Azure Deployment

### Option 1: Azure Developer CLI (Recommended)

```bash
# Login to Azure
azd auth login

# Initialize and deploy
azd up
```

### Option 2: Manual Deployment

```bash
# Login to Azure
az login

# Create resource group
az group create --name anchor-rg --location eastus

# Deploy infrastructure
az deployment group create \
  --resource-group anchor-rg \
  --template-file infra/bicep/main.bicep \
  --parameters appName=anchor-starter \
               environmentName=dev \
               sqlAdminLogin=sqladmin \
               sqlAdminPassword='YourSecurePassword123!'
```

## 🔒 Security

- Environment variables for sensitive configuration
- SQL injection prevention via parameterized queries
- XSS protection in frontend JavaScript
- HTTPS enforced in production
- Secure password requirements for SQL Server
- Azure Managed Identity support (configure in production)

## 📚 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Example Endpoints

- `GET /health` - Health check
- `GET /health/db` - Database health check
- `GET /api/items/` - List all items
- `POST /api/items/` - Create new item
- `GET /api/items/{id}` - Get specific item
- `PUT /api/items/{id}` - Update item
- `DELETE /api/items/{id}` - Delete item

## 🔧 Configuration

Configuration is managed through environment variables. See `.env.example` for all available options.

Key settings:
- `DB_SERVER` - Database server address
- `DB_NAME` - Database name
- `DB_USER` - Database username
- `DB_PASSWORD` - Database password
- `STORAGE_ACCOUNT_NAME` - Azure Storage account name
- `DEBUG` - Enable debug mode (development only)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- PicoCSS for the minimal CSS framework
- Microsoft Azure for cloud infrastructure
- The Python community for amazing tools and libraries
