import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        with open('octofit-tracker/backend/octofit_tracker/test_data.json') as f:
            data = json.load(f)

        # Users
        email_to_user = {}
        for user_data in data['users']:
            user, created = User.objects.get_or_create(email=user_data['email'], defaults={
                'name': user_data['name'],
                'password': user_data['password']
            })
            email_to_user[user.email] = user

        # Teams
        for team_data in data['teams']:
            members = [email_to_user[email] for email in team_data['members'] if email in email_to_user]
            team, created = Team.objects.get_or_create(name=team_data['name'])
            team.save()
            team.members.add(*members)

        # Activities
        for activity_data in data['activity']:
            user = email_to_user.get(activity_data['user'])
            if user:
                Activity.objects.get_or_create(
                    user=user,
                    activity_type=activity_data['activity_type'],
                    duration=activity_data['duration'],
                    date=parse_datetime(activity_data['date'])
                )

        # Leaderboard
        for leaderboard_data in data['leaderboard']:
            team = Team.objects.filter(name=leaderboard_data['team']).first()
            if team:
                Leaderboard.objects.get_or_create(
                    team=team,
                    points=leaderboard_data['points']
                )

        # Workouts
        for workout_data in data['workouts']:
            user = email_to_user.get(workout_data['user'])
            if user:
                Workout.objects.get_or_create(
                    user=user,
                    workout_type=workout_data['workout_type'],
                    details=workout_data['details'],
                    date=parse_datetime(workout_data['date'])
                )

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
