# Generated by Django 5.0.4 on 2024-04-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_medium_name_alter_style_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medium',
            name='name',
            field=models.CharField(choices=[('ACR', 'Acrylic'), ('BOD', 'Body Art / Tattoo'), ('CER', 'Ceramics'), ('CHA', 'Charcoal'), ('COL', 'Collage'), ('DIG', 'Digital Art'), ('DRW', 'Drawing'), ('GLS', 'Glass Art'), ('H2O', 'Water Color'), ('INK', 'Ink / Sumi-e'), ('INS', 'Installation Art'), ('LTR', 'Leather Work'), ('MIX', 'Mixed Media'), ('MOS', 'Mosaic'), ('MUR', 'Mural / Graffiti'), ('MTL', 'Metal Work'), ('OIL', 'Oil Painting'), ('PAP', 'Paper Art / Origami'), ('PAS', 'Pastel'), ('PERF', 'Performance Art'), ('PHO', 'Photography'), ('PRI', 'Print Making'), ('SND', 'Sound Art / Music'), ('SCU', 'Sculpture'), ('TXT', 'Textile Art / Fiber Arts'), ('TYP', 'Typography'), ('OTH', 'Other')], default='ACR', max_length=75),
        ),
        migrations.AlterField(
            model_name='style',
            name='name',
            field=models.CharField(choices=[('ABS', 'Abstract'), ('ART', 'Art Nouveau'), ('BOT', 'Botanical'), ('CLA', 'Classical'), ('CON', 'Contemporary'), ('CON', 'Contemporary'), ('CUB', 'Cubism'), ('EXP', 'Experimental'), ('FOL', 'Paper Folding / Papercraft'), ('IMP', 'Impressionism'), ('KNI', 'Knit / Crochet'), ('MIN', 'Minimalism'), ('MUS', 'Music'), ('NAR', 'Narrative'), ('PIX', 'Pixel Art'), ('POP', 'Pop Art'), ('POR', 'Portrait'), ('POR', 'Porcelain / Stoneware'), ('POS', 'Post Modernism'), ('REA', 'Realism'), ('ROM', 'Romanticism'), ('SKE', 'Sketch'), ('SOU', 'Interactive Sound Installation'), ('STR', 'Street Art'), ('SUR', 'Surrealism'), ('THE', 'Theatrical'), ('THA', 'Thangka'), ('TOO', 'Tattoo / Henna'), ('QUI', 'Quilting / Weaving'), ('VIN', 'Vintage'), ('OTH', 'Other')], default='ABS', max_length=75),
        ),
    ]
