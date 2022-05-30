from django.contrib import admin

from .models import Company, Review, Social, Profile, Skill, Post, Comment

# Register your models here.
admin.site.register(Company)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(Like)