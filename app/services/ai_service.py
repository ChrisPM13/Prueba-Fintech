def extract_info_from_text(application):
    """
    Mock de extracción de información de documento que
    devuelve los mismos datos que el cliente ingresó en la solicitud,
    simulando que el OCR reconoce la info correctamente.
    """
    return {
        "nombre": application.name,
        "direccion": application.address_input,
        "fecha": "2024-01-01"  # simulamos que el comprobante tiene fecha fija
    }