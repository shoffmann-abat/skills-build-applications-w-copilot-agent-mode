from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from pymongo import MongoClient

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		# Lösche alle Daten
		User.objects.all().delete()
		Team.objects.all().delete()
		Activity.objects.all().delete()
		Workout.objects.all().delete()
		Leaderboard.objects.all().delete()


		# Teams
		Team.objects.create(name='Marvel')
		Team.objects.create(name='DC')

		# Users
		User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
		User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
		User.objects.create(name='Batman', email='batman@dc.com', team='DC')
		User.objects.create(name='Superman', email='superman@dc.com', team='DC')

		# Activities
		Activity.objects.create(user_email='ironman@marvel.com', type='Running', duration=30, date='2026-01-01')
		Activity.objects.create(user_email='batman@dc.com', type='Cycling', duration=45, date='2026-01-02')

		# Workouts
		Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for=['ironman@marvel.com', 'batman@dc.com'])
		Workout.objects.create(name='Power Yoga', description='Yoga for super strength', suggested_for=['superman@dc.com', 'cap@marvel.com'])

		# Leaderboard
		Leaderboard.objects.create(team='Marvel', points=100)
		Leaderboard.objects.create(team='DC', points=120)

		# Unique Index auf Email
		client = MongoClient('localhost', 27017)
		db = client['octofit_db']
		db['octofit_tracker_user'].create_index('email', unique=True)

		self.stdout.write(self.style.SUCCESS('Testdaten und Index erfolgreich erstellt!'))