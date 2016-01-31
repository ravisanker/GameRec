from tastypie.resources import ModelResource
from GameRec.models import Games
from django.http import JsonResponse
import operator
import sys

class EntryResource(ModelResource):
	class Meta:
		queryset = Games.objects.all()
		resource_name = 'entry'


class Recommender():

	def similarto(request):
		GENRE_WEIGHT = 0.75
		YEAR_WEIGHT = 0.20
		PUBLISHER_WEIGHT = 0.05
		genres = []
		games = {}
		final_list =[]
		all_games = Games.objects.all()
		search_id = request.GET.get('id', '')
		if (search_id != ''):
			for game in all_games:
				if (game.id == int(search_id)):
					genres = game.genre.split(',')
					year_released = game.year_released
					publisher = game.publisher
					break
			for game in all_games:				
				similarity_index = 0.0
				similar_genre_count = 0
				game_genres = game.genre.split(',')
				for genre1 in game_genres:
					for genre2 in genres:
						if genre1.strip() == genre2.strip():
							similar_genre_count += 1
				if (abs(year_released - game.year_released) <= 2):
					similarity_index += YEAR_WEIGHT
				if(publisher == game.publisher):
					similarity_index += PUBLISHER_WEIGHT

				similarity_index += GENRE_WEIGHT * (similar_genre_count/len(genres))
				games[game.title] = similarity_index
	
			for gamex in sorted(games, key = games.get, reverse = True):
				each_game = {}
				each_game['title'] = gamex
				each_game['similarity_index'] = games[gamex]
				final_list.append(each_game)
		return JsonResponse({"similar_games":final_list})					