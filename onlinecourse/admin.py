from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner,Question,Choice,Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
    # LessonInline starts working when Django is displaying a Course form 
    # (Add Course or Edit Course)
#  displays lessons inside the course admin page 
# lessonInline is used to manage lesson objects

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]  #show/edit ,we embedded lesson editing inside course editing
    list_display = ('name', 'pub_date') #columns showsn in course_list view in course_list page
    list_filter = ['pub_date'] #filter by date
    search_fields = ['name', 'description'] #search box search fileds showuld be these
# Django Admin automatically generates a search box in the admin interface.

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# <HINT> Register Question and Choice models here
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra=2

class QuestionInline(admin.StackedInline):
		model = Question
		extra = 2

class QuestionAdmin(admin.ModelAdmin):
		inlines = [ChoiceInline]
		list_display = ['content']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

# Without Inline
# Admin
# ├── Courses
# └── Lessons

# To add a lesson:

# Open Course
# Save Course
# Go to Lessons
# Add Lesson separately

# With Inline

# When you click:

# Admin
# └── Courses
#      └── Django Course