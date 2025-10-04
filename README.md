# Simulated Collections API

This project is a FastAPI-based REST API for managing clients, cards, and collections (cobros), with MongoDB as the database and Docker support for easy deployment.

## Features
- FastAPI REST endpoints for clients, cards, and collections
- MongoDB integration using Motor
- Pydantic models for validation
- Business logic for collection approval
- Automated tests with pytest
- OpenAPI documentation generation
- Docker and Docker Compose support
- Makefile for common development tasks

## Setup

### Clone the repository
```sh
git clone <your-repo-url>
cd simulated-collections
```

### Build and run with Docker
```sh
make docker-build
make docker-up
```

### Run tests
```sh
make tests
```

### Format code
```sh
make format
```

### Generated OpenAPI documentation
```
Visit this url once the application is running
http://127.0.0.1:8000/docs
```

## Environment Variables
See `.env.local` for required environment variables for local configuration:
```
ENV=development
DEBUG=True
MONGODB_HOST=mongodb
MONGODB_PORT=27017
MONGODB_DB=simulated-collections
MONGODB_USER=collections
MONGODB_PASSWORD=collpass
```

## Project Structure
```
database/
  models/
  repositories/
services/
routes/
.env.local
Makefile
Dockerfile
docker-compose.yml
main.py
```

## API Endpoints
- `/clientes` - CRUD for clients
- `/tarjetas` - CRUD for cards
- `/cobros` - CRUD for collections, refund endpoint


### Crear cliente

```json
{
    "nombre": "Antonio de Jesus",
    "email": "shilong_92@hotmail.com",
    "telefono": "5556784311"
}
```

## Crear tarjetas de pruebas


```json
{
    "cliente_id": YOUR_CLIENT_ID,
    "pan": "4006257249775562",
    "last4": "5562",
    "bin": "4"
}


{
    "cliente_id": YOUR_CLIENT_ID,
    "pan": "5785539506641734",
    "last4": "1734",
    "bin": "5"
}

{
    "cliente_id": YOUR_CLIENT_ID,
    "pan": "6721686452722417",
    "last4": "2417",
    "bin": "5"
}

```

## Reglas de aprobación de un pago

- El monto debe ser mayor a cero y menor igual que 500000.00
- EL valor del campo codigo_motivo no debe estár en la lista de motivos de rechazo
```
CODIGO_MOTIVO_LIST = [
    "01",  # Insufficient funds
    "02",  # Card expired
    "03",  # Invalid card
    "04",  # Suspected fraud
    "05",  # Card blocked
    "06",  # Limit exceeded
    "07",  # Technical error
    "08",  # Duplicate transaction
    "09",  # Invalid amount
]
```
- El cobro se aprueba si la tarjeta no tiene mas de 2 cobros declinados en el mes actual

## License
MIT
