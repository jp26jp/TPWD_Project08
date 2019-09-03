import json

from django.core.management.base import BaseCommand

from minerals.models import Mineral


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('minerals.json', encoding='utf-8') as file:
            minerals = json.load(file)

        for mineral in minerals:
            category = ""
            formula = ""
            strunz_classification = ""
            unit_cell = ""
            color = ""
            crystal_habit = ""
            mohs_scale_hardness = ""
            crystal_system = ""
            crystal_symmetry = ""
            cleavage = ""
            luster = ""
            streak = ""
            diaphaneity = ""
            optical_properties = ""
            refractive_index = ""
            specific_gravity = ""
            group = ""
            if mineral['category']:
                category = mineral['category']
            if 'formula' in mineral:
                formula = mineral['formula']
            if 'strunz_classification' in mineral:
                strunz_classification = mineral['strunz_classification']
            if 'unit_cell' in mineral:
                unit_cell = mineral['unit_cell']
            if 'color' in mineral:
                color = mineral['color']
            if 'crystal_habit' in mineral:
                crystal_habit = mineral['crystal_habit']
            if 'mohs_scale_hardness' in mineral:
                mohs_scale_hardness = mineral['mohs_scale_hardness']
            if 'crystal_system' in mineral:
                crystal_system = mineral['crystal_system']
            if 'crystal_symmetry' in mineral:
                crystal_symmetry = mineral['crystal_symmetry']
            if 'cleavage' in mineral:
                cleavage = mineral['cleavage']
            if 'luster' in mineral:
                luster = mineral['luster']
            if 'streak' in mineral:
                luster = mineral['streak']
            if 'diaphaneity' in mineral:
                diaphaneity = mineral['diaphaneity']
            if 'optical_properties' in mineral:
                optical_properties = mineral['optical_properties']
            if 'refractive_index' in mineral:
                refractive_index = mineral['refractive_index']
            if 'specific_gravity' in mineral:
                specific_gravity = mineral['specific_gravity']
            if 'group' in mineral:
                group = mineral['group']
            Mineral(
                name=mineral['name'],
                image_filename=mineral['image_filename'],
                image_caption=mineral['image_caption'],
                category=category,
                formula=formula,
                strunz_classification=strunz_classification,
                unit_cell=unit_cell,
                color=color,
                crystal_habit=crystal_habit,
                mohs_scale_hardness=mohs_scale_hardness,
                crystal_system=crystal_system,
                crystal_symmetry=crystal_symmetry,
                cleavage=cleavage,
                luster=luster,
                streak=streak,
                diaphaneity=diaphaneity,
                optical_properties=optical_properties,
                refractive_index=refractive_index,
                specific_gravity=specific_gravity,
                group=group
            ).save()
        self.stdout.write(self.style.SUCCESS('Mineral data has been successfully added!'))

