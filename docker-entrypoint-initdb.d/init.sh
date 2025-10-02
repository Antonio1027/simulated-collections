  #!/usr/bin/env bash
  echo "Creating MongoDB users..."
  mongosh --authenticationDatabase admin --host localhost -u root -p rootpassword --eval "db.getSiblingDB('simulated-collections').createUser({user: 'collections', pwd: 'collpass', roles: [{role: 'readWrite', db: 'simulated-collections'}]});"
  echo "MongoDB users created."