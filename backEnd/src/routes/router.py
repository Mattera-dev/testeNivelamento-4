from src.controller import providers

def loadRoutes(app):
    app.add_url_rule("/search", "search_provider", providers.search, methods=["GET"]) 
