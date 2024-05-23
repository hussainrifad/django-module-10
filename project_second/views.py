from django.shortcuts import render
from datetime import datetime

def main(request):
    playerInfo = {
        'total_players' : 6,
        'playerList' : [
            {
                'name' : 'Mahmud',
                'age' : 20,
                'address' : 'London',
                'description' : 'A soccer player profile template is a document that provides an outline of the information needed to create a detailed profile of a soccer player.',
                'nationality' : 'Algerian',
                'recentDate' : datetime.today()
            },
            {
                'name' : 'Absar',
                'age' : 38,
                'address' : 'Moscow',
                'description' : 'A soccer player profile template is a document that provides an outline of the information needed to create a detailed profile of a soccer player.',
                'nationality' : 'Qatari',
                'recentDate' : datetime.today()
            },
            {
                'name' : 'Muba',
                'age' : 22,
                'address' : 'Saint Petersburg',
                'description' : 'A soccer player profile template is a document that provides an outline of the information needed to create a detailed profile of a soccer player.',
                'nationality' : 'Egyptian',
                'recentDate' : datetime.today()
            },
            {
                'name' : 'Ashiq',
                'age' : 18,
                'address' : 'Oslo',
                'description' : 'A soccer player profile template is a document that provides an outline of the information needed to create a detailed profile of a soccer player.',
                'nationality' : 'Indian',
                'recentDate' : datetime.today()
            },
            {
                'name' : 'Nihat',
                'age' : 44,
                'address' : 'Paris',
                'description' : 'A soccer player profile template is a document that provides an outline of the information needed to create a detailed profile of a soccer player.',
                'nationality' : 'Bangladeshi',
                'recentDate' : datetime.today()
            },
            {
                'name' : 'Leom',
                'age' : 34,
                'address' : 'Berlin',
                'description' : 'A soccer player profile template is a document that provides an outline of the information needed to create a detailed profile of a soccer player.',
                'nationality' : 'Moroccan',
                'recentDate' : datetime.today()
            }
        ]
    }
    return render(request, 'main.html', playerInfo)