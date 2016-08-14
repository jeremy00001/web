from django.http import HttpResponse

from model.models import Test


def testdb(request):
    test1 = Test(name='w3cschool.cc')
    test1.save()
    return HttpResponse("<p>Data inserted</p>")


def getdb(request):
    # intial
    response = ""
    response1 = ""

    # select all
    rlist = Test.objects.all()

    # filter
    response2 = Test.objects.filter(id=1)

    #
    response3 = Test.objects.get(id=1)

    # OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    Test.objects.order_by("id")

    Test.objects.filter(name="w3cschool.cc").order_by("id")

    for var in rlist:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
