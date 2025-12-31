from django.shortcuts import render,redirect

from app1.models import Survey_form


def user(request):                                   # METHOD 1
    if request.method == 'POST':
        data = Survey_form(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            Native=request.POST.get('Native'),
            degree=request.POST.get('degree'),
            sleep_hours=request.POST.get('sleep_hours'),
            social_media_hours=request.POST.get('social_media_hours'),
            social_media=request.POST.get('social_media'),
            eat_on_time=request.POST.get('eat_on_time'),
            physical_activity=request.POST.get('physical_activity'),
            how_productive=request.POST.get('how_productive'),
            experiencing_stress=request.POST.get('experiencing_stress'),
            loneliness=request.POST.get('loneliness'),
            overthinking=request.POST.get('overthinking'),
            self_proudness=request.POST.get('self_proudness'),
            learn_new=request.POST.get('learn_new'),
            want_in_life=request.POST.get('want_in_life'),
            felt_no_potential=request.POST.get('felt_no_potential'),
            employement_status=request.POST.get('employement_status'),
            career_pressure=request.POST.get('career_pressure'),
            financial_stability=request.POST.get('financial_stability'),
            money_management=request.POST.get('money_management'),
            mental_health_financially=request.POST.get('mental_health_financially'),
            self_dependencies=request.POST.get('self_dependencies'),
            reflect_for_past=request.POST.get('reflect_for_past')
        )
        data.save()
        return redirect('thankyou')  # You can create a thank-you page
    return render(request,'template1.html')

def thankyou(req):
    return render(req,'thankyou.html')