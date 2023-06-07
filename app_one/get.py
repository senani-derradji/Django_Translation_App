def getData(request) -> str :
    '''
    This Function Get String Data from Template and save it in variable Data
    '''

    if request.method == "POST":
        text = request.POST.get("input_text")
        language = str(request.POST.get("languageSelect"))
        return text
