# Stage 1: Build the application
FROM node:18-alpine AS build

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN npm install

# Build the application (if there's a build step, if not you can omit this)
RUN npm run build

# Stage 2: Run the application
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=build /app /app

# Expose the port the development server runs on
EXPOSE 5173

# Run the development server
CMD ["npm", "run", "dev", "--", "--host"]
