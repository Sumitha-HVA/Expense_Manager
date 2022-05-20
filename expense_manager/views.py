from unicodedata import name
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Vendor, Expenses
from .serializers import EmployeeSerializer, VendorSerializer, ExpensesSerializer


class EmpList(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    # def get(self, request,*args, **kwargs):
    #     try:
    #         emp_code = request.query_params["emp_code"]
    #         if emp_code != None:
    #             employee = Employee.objects.get(emp_code= emp_code)
    #             serializer = EmployeeSerializer(employee)
    #     except:
    #         employees = self.get()
    #         serializer = EmployeeSerializer(employees, many=True)

    def post(self, request):
        empobj = EmployeeSerializer(data=request.data)
        if empobj.is_valid():
            empobj.save()
            # return Response(empobj.data, status=status.HTTP_201_CREATED,)
            return Response("Employee Created")
        return Response(empobj.errors, status =status.HTTP_400_BAD_REQUEST)



class EmpDetail(APIView):

    def get(self, request, pk):
        data = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data)
        return Response(serializer.data)



class VendorList(APIView):

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        vendorobj = VendorSerializer(data=request.data)
        if vendorobj.is_valid():
            vendorobj.save()
            # return Response(empobj.data, status=status.HTTP_201_CREATED,)
            return Response("Vendor Created")
        return Response(vendorobj.errors, status =status.HTTP_400_BAD_REQUEST)



class ExpenseList(APIView):

    def get(self, request):
        expenses = Expenses.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        expenseobj = ExpensesSerializer(data=request.data)
        if expenseobj.is_valid():
            expenseobj.save()
            # return Response(empobj.data, status=status.HTTP_201_CREATED,)
            return Response("Expense Created")
        return Response(expenseobj.errors, status =status.HTTP_400_BAD_REQUEST)



class ExpenseDetail(APIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Expenses.objects.all()
        name = self.request.query_params.get('name', None)
        return queryset.filter(name=name)


