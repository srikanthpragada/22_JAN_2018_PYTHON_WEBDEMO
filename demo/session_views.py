from django.shortcuts import render, redirect


def list_names(request):
    # either take existing names or empty list
    if 'names' in request.session:
        names = request.session['names']
    else:
        names = []

    if request.method == "POST":
        # add name to list
        fullname = request.POST['fullname']
        names.append(fullname)
        # create key names in the session
        request.session['names'] = names

    return render(request, 'demo/session_names.html', {'names': names})
