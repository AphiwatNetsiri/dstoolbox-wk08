FROM nginx:alpine
# Copy the single static page into nginx html folder
COPY index.html /usr/share/nginx/html/index.html
# Expose port 80 for HTTP
EXPOSE 80
# Use default nginx command
CMD ["nginx", "-g", "daemon off;"]
