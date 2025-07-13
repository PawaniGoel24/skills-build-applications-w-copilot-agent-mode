# Tests for OctoFit Tracker
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test2@example.com', name='Test User2', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-07-13T00:00:00Z')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team2')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='test3@example.com', name='Test User3', password='testpass')
        workout = Workout.objects.create(user=user, workout_type='cardio', details='30 min run', date='2025-07-13T00:00:00Z')
        self.assertEqual(workout.workout_type, 'cardio')
