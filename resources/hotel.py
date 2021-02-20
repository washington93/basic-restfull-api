from flask_restful import Resource, reqparse

hoteis = [
    {'hotel_id': '1', 'name': 'Alpha Hotel', 'stars':5, 'daily' :420},
    {'hotel_id': '2', 'name': 'Beta Hotel', 'stars':4.3, 'daily' :410},
    {'hotel_id': '3', 'name': 'Omega Hotel', 'stars':4, 'daily' :400},
]

class Hoteis(Resource):
    def get(self):
        return hoteis, 200

    def post(self):
        args = reqparse.RequestParser()
        args.add_argument('name')
        args.add_argument('stars')
        args.add_argument('daily')
        
        data = args.parse_args()

        newHotel = {
            'hotel_id': len(hoteis),
            'name': data['name'],
            'stars': data['stars'],
            'daily': data['daily']
        }

        hoteis.append(newHotel)
    
        return newHotel, 201

class Hotel(Resource):
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel,200
        return None
        
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel is not None:
            return hotel
        return {'message': f'{hotel_id} is not found'},200

    def put(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel is not None:
            args = reqparse.RequestParser()
            args.add_argument('name')
            args.add_argument('stars')
            args.add_argument('daily')
            data = args.parse_args()
            newHotel = {
                'hotel_id': hotel_id,
                'name': data['name'],
                'stars': data['stars'],
                'daily': data['daily']
            }

            hotel.update(newHotel)
            return newHotel, 200
        return {'message' : 'invalid argument.'}

    def delete(self, hotel_id):
        print(hotel_id)
        hotel = Hotel.find_hotel(hotel_id)
        print(hotel)
        if hotel is not None:
            global hoteis
            hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
            return {'message': 'Hotel deleted'}
        return {'message': 'hotel is not found'},200
        
