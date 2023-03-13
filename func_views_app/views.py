from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(["POST","GET"])
def funkcija1(request):
 ime=request.data.get("ime",None)
 dolzhina=len(ime)
 ime_golemi=ime.upper()
 ime_meshano=ime.swapcase()
 data={"ime":ime,
       "dolzhina":dolzhina,
       "ime_so_golemi_bukvi":ime_golemi,
       "ime_obratno_mali_golemi":ime_meshano}
 return Response(data)


@api_view(["POST"])
def funkcija2(request):
 broj1=request.data.get("broj1",0)
 broj2=request.data.get("broj2",0)
 perimetar=2*broj1+2*broj2
 ploshtina=broj1*broj2
 data={"info": "Ploshtinata i perimetarot na {} i {} se {} i {} soodvetno".format(broj1,broj2,ploshtina,perimetar),
      "ploshtina":ploshtina,
      "perimetar":perimetar
      }
 return Response(data)

@api_view(["GET"])
def funkcija3(request):
 broj=int(request.GET.get("broj1",None))
 if broj%2==0:
    data = {"poraka":" {}  e paren".format(broj)
                        }
 else:
    data = {"poraka":" {}  e neparen".format(broj)
                        }
 return Response(data)
 

 