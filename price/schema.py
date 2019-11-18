from graphene_django import DjangoObjectType
import graphene
from dashboard.models import * 
from account.models import *

class Products(DjangoObjectType):
    class Meta:
        model = Product

class Companies(DjangoObjectType):
    class Meta:
        model = Company




class Categories(DjangoObjectType):
    class Meta:
        model = Category 

                      



class Query(graphene.ObjectType):
	products = graphene.List(Products)
	categories = graphene.List(Categories)
	companies = graphene.List(Companies)


	def resolve_companies(self, info):
	    return Company.objects.all()

	def resolve_categories (self, info):
	    return Category.objects.all()    

	def resolve_producs(self, info):
	    return Product.objects.all()    



schema = graphene.Schema(query=Query)