# Generated by Django 3.2.11 on 2022-01-13 19:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import main.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "category_name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Nom de la catégorie"
                    ),
                ),
                ("summary", models.TextField()),
                ("image", models.ImageField(upload_to="images/", verbose_name="Photo")),
                ("category_slug", models.SlugField(unique=True)),
            ],
            options={"verbose_name": "Catégorie", "verbose_name_plural": "Catégories",},
            bases=(models.Model, main.mixins.BaseModelMixin),
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "item_name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Nom de la recette"
                    ),
                ),
                ("summary", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="images/", verbose_name="Photo")),
                (
                    "content",
                    models.TextField(
                        default='<p style="margin: 0px; font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\'; text-align: left;"><span style="font-family: helvetica, arial, sans-serif;"><strong style="caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-size: 32px;"><span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">&nbsp;</span></span></strong><strong style="caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-size: 32px;"><span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">✅ Ingr&eacute;dients</span></span></strong></span></p>\n<ol>\n   <li style="font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\';"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Ingredient1</span></li>\n   <li style="font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\';"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Ingredient2</span></li>\n</ol>\n<p>&nbsp;</p>\n<p><span style="font-family: helvetica, arial, sans-serif;"><strong style="caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-size: 32px;"><span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">🔪&nbsp;</span></span></strong><strong style="caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-size: 32px;"><span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">Pr&eacute;paration</span></span></strong></span></p>\n<ol>\n   <li style="font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\';"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Instruction1</span></li>\n   <li style="font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\';"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Instruction2</span></li>\n</ol>\n<p>&nbsp;</p>\n<p><span style="font-family: helvetica, arial, sans-serif;"><strong style="caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-size: 32px;"><span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">🕗&nbsp;</span></span></strong><strong style="caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-size: 32px;"><span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">Cuisson</span></span></strong></span></p>\n<ol>\n   <li style="font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\';"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Instruction1</span></li>\n   <li style="font-stretch: normal; font-size: 12px; line-height: normal; font-family: \\\'Helvetica Neue\\\';"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Instruction2</span></li>\n</ol>\n<p>&nbsp;</p>\n<p style="box-sizing: inherit; line-height: 2rem; caret-color: rgba(0, 0, 0, 0.87); color: rgba(0, 0, 0, 0.87); font-family: -apple-system, BlinkMacSystemFont, \\\'Segoe UI\\\', Roboto, Oxygen-Sans, Ubuntu, Cantarell, \\\'Helvetica Neue\\\', sans-serif; font-size: 15px;">&nbsp;</p>\n<p style="text-align: center;"><span style="font-size: 14pt; font-family: helvetica, arial, sans-serif;">Bon app<span style="box-sizing: inherit;"><span lang="FR" style="box-sizing: inherit;">&eacute;</span></span>tit! 👩🏻&zwj;🍳</span></p>',
                        verbose_name="Contenu",
                    ),
                ),
                (
                    "date_published",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date published"
                    ),
                ),
                ("item_slug", models.SlugField(unique=True)),
                ("views", models.IntegerField(default=0)),
                (
                    "category_name",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="main.category",
                        verbose_name="Catégorie",
                    ),
                ),
            ],
            options={"verbose_name": "Recettes", "verbose_name_plural": "Recettes",},
            bases=(models.Model, main.mixins.BaseModelMixin),
        ),
    ]
