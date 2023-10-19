from engine import engine,session
from sqlalchemy.orm import sessionmaker
from create_table import City 

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cities.models import City
from psycopg import cursor

@api_view(['POST'])
def create_city(request):
    print(request.data)
    city_name = request.data.get('name')
    population = request.data.get('population')
    print(city_name,population)

    if city_name is None or population is None:
        return Response({'error': 'Both name and population are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        city = City(name=city_name, population=int(population))

        # with session() as session:
        session.add(city)
        session.commit()

        return Response({'message': 'City created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': 'City creation failed.', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.http import JsonResponse
from django.db import connection

@api_view(['GET'])
def List_city(request):
    # Use Django's database connection and cursor
    with connection.cursor() as cursor:
        try:
            # Retrieve all City objects from the database
            cursor.execute("SELECT * FROM cities")
            results = cursor.fetchall()
            print(results)

            # Convert the results to a list of dictionaries for JsonResponse
            city_list = [dict(zip([col[0] for col in cursor.description], row)) for row in results]

            return JsonResponse(city_list, safe=False)  # Set safe=False to allow non-dict objects to be serialized
        except Exception as e:
            return JsonResponse({'error': 'Error retrieving cities.', 'details': str(e)}, status=500)
