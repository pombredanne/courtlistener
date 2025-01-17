# -*- coding: utf-8 -*-


from django.db import migrations, models

import cl.lib.model_helpers
import cl.lib.storage


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0045_add_party_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='recapdocument',
            name='is_free_on_pacer',
            field=models.BooleanField(help_text='Is this item freely available as an opinion on PACER?', db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='recapdocument',
            name='filepath_local',
            field=models.FileField(help_text='The path of the file in the local storage area.', storage=cl.lib.storage.IncrementingFileSystemStorage(), max_length=1000, upload_to=cl.lib.model_helpers.make_pdf_path, blank=True),
        ),
    ]
