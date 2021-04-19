from django.test import TestCase

# Create your tests here.

    # def serialize(self):
    #     # print(self.rank.airforce_rank)
    #     return {
    #         "pk": self.pk,
    #         "rank": self.rank.airforce_rank,
    #         "first_name_eng": self.first_name_eng,
    #         "last_name_eng": self.last_name_eng,
    #         "first_name_thai": self.first_name_thai,
    #         "last_name_thai": self.last_name_thai,
    #         "date_birth": self.date_birth,
    #         "line_id": self.line_id,
    #         "telephone": self.telephone,
    #         "email": self.email,
    #         "picture": f'{self.picture}',
    #         "division": f'{self.division}',
    #         "position": f'{self.position}',
    #         "position_other": self.position_other,
    #         "lucky_number": self.lucky_number,
    #         "afaps": self.afaps,
    #         "passport": self.passport,
    #         "visa": self.visa,
    #         "still_service": self.still_service,
    #         "is_pilot": self.is_pilot,
    #         "create_at": self.create_at,
    #         "update": self.update.strftime("%b %d %Y, %I:%M %p"),
    #     }


#storage.py
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os

# class OverwriteStorage(FileSystemStorage):

#     def get_available_name(self, name):
#         """Returns a filename that's free on the target storage system, and
#         available for new content to be written to.

#         Found at http://djangosnippets.org/snippets/976/

#         This file storage solves overwrite on upload problem. Another
#         proposed solution was to override the save method on the model
#         like so (from https://code.djangoproject.com/ticket/11663):

#         def save(self, *args, **kwargs):
#             try:
#                 this = MyModelName.objects.get(id=self.id)
#                 if this.MyImageFieldName != self.MyImageFieldName:
#                     this.MyImageFieldName.delete()
#             except: pass
#             super(MyModelName, self).save(*args, **kwargs)
#         """
#         # If the filename already exists, remove it as if it was a true file system
#         if self.exists(name):
#             os.remove(os.path.join(settings.MEDIA_ROOT, name))
#         return name