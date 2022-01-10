# Generated by Django 4.0.1 on 2022-01-10 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_login_tour_locations_tour_packages_and_more'),
        ('shangkai_app', '0011_hotel_category_my_trips_hotspot_category_images_and_more'),
        ('users', '0017_auto_20211119_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Cab_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user_ip', models.CharField(max_length=255, null=True, verbose_name='user_ip')),
                ('cab_bookid', models.CharField(default='0', max_length=255, null=True, verbose_name='cab_bookid')),
                ('check_in_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_date')),
                ('check_in_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_time')),
                ('check_out_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_date')),
                ('check_out_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_time')),
                ('start_from', models.CharField(max_length=255, null=True, verbose_name='start_from')),
                ('end_trip', models.CharField(max_length=255, null=True, verbose_name='end_trip')),
                ('distance', models.CharField(max_length=255, null=True, verbose_name='distance')),
                ('amount_booking', models.CharField(max_length=255, null=True, verbose_name='amount')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('booking_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('car_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.cabs_reg')),
                ('driver_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.driver_reg')),
            ],
            options={
                'verbose_name': 'Cab Booking',
                'verbose_name_plural': 'Cab Booking',
            },
        ),
        migrations.CreateModel(
            name='User_Cab_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('check_in_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_date')),
                ('check_in_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_time')),
                ('check_out_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_date')),
                ('check_out_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_time')),
                ('start_from', models.CharField(max_length=255, null=True, verbose_name='start_from')),
                ('end_trip', models.CharField(max_length=255, null=True, verbose_name='end_trip')),
                ('distance', models.CharField(max_length=255, null=True, verbose_name='distance')),
                ('amount_booking', models.CharField(max_length=255, null=True, verbose_name='amount')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('booking_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('car_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.cabs_reg')),
                ('driver_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.driver_reg')),
            ],
            options={
                'verbose_name': 'Cab Cart',
                'verbose_name_plural': 'Cab Cart',
            },
        ),
        migrations.CreateModel(
            name='User_Cab_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('payment_id', models.CharField(max_length=255, null=True, verbose_name='payment_id')),
                ('payment_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('cab_booking', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user_cab_booking')),
            ],
            options={
                'verbose_name': 'User Cab Payments',
                'verbose_name_plural': 'User Cab Payments',
            },
        ),
        migrations.CreateModel(
            name='User_Guide_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('booking_date', models.DateField(max_length=255, null=True, verbose_name='booking_date')),
                ('guide_amount', models.CharField(max_length=255, null=True, verbose_name='guide_ammount')),
                ('razorpay_id', models.CharField(default='0', max_length=255, null=True, verbose_name='razorpay_id')),
                ('status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('client_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.user_register')),
                ('guide_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.tourguide_reg')),
            ],
            options={
                'verbose_name': 'Tour Guide Booking',
                'verbose_name_plural': 'Tour Guide Booking',
            },
        ),
        migrations.CreateModel(
            name='User_Hotel_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user_ip', models.CharField(max_length=255, null=True, verbose_name='user_ip')),
                ('hotel_bookid', models.CharField(default='0', max_length=255, null=True, verbose_name='hotel_bookid')),
                ('check_in_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_date')),
                ('check_in_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_time')),
                ('check_out_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_date')),
                ('check_out_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_time')),
                ('guest_no', models.CharField(default='0', max_length=255, null=True, verbose_name='guests')),
                ('rooms', models.CharField(default='0', max_length=255, null=True, verbose_name='rooms')),
                ('amount_booking', models.CharField(default='0', max_length=255, null=True, verbose_name='amount_booking')),
                ('booking_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('hotel_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.reg_hotel')),
                ('room_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.room_register')),
            ],
            options={
                'verbose_name': 'Hotel Booking',
                'verbose_name_plural': 'Hotel Booking',
            },
        ),
        migrations.CreateModel(
            name='User_Hotel_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('check_in_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_date')),
                ('check_in_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_in_time')),
                ('check_out_date', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_date')),
                ('check_out_time', models.CharField(default='0', max_length=255, null=True, verbose_name='check_out_time')),
                ('guest_no', models.CharField(default='0', max_length=255, null=True, verbose_name='guests')),
                ('rooms', models.CharField(default='0', max_length=255, null=True, verbose_name='rooms')),
                ('amount_booking', models.CharField(default='0', max_length=255, null=True, verbose_name='amount_booking')),
                ('booking_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('hotel_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.reg_hotel')),
                ('room_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.room_register')),
            ],
            options={
                'verbose_name': 'Hotel Cart',
                'verbose_name_plural': 'Hotel Cart',
            },
        ),
        migrations.CreateModel(
            name='User_Hotel_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('payment_id', models.CharField(max_length=255, null=True, verbose_name='payment_id')),
                ('payment_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('hotel_booking', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user_hotel_booking')),
            ],
            options={
                'verbose_name': 'User Hotel Payments',
                'verbose_name_plural': 'User Hotel Payments',
            },
        ),
        migrations.CreateModel(
            name='User_Hotspots_Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('booking_date', models.DateField(max_length=255, null=True, verbose_name='booking_date')),
                ('booking_amount', models.CharField(max_length=255, null=True, verbose_name='booking_amount')),
                ('razorpay_id', models.CharField(default='0', max_length=255, null=True, verbose_name='razorpay_id')),
                ('status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Hotspots Bookings',
                'verbose_name_plural': 'Hotspots Bookings',
            },
        ),
        migrations.CreateModel(
            name='User_Hotspots_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('booking_date', models.DateField(max_length=255, null=True, verbose_name='booking_date')),
                ('cart_amount', models.CharField(max_length=255, null=True, verbose_name='cart_ammount')),
                ('status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('hostpots_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='shangkai_app.hot_spots')),
            ],
            options={
                'verbose_name': 'Hotspots Cart',
                'verbose_name_plural': 'Hotspots Cart',
            },
        ),
        migrations.CreateModel(
            name='User_Trip_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('trip_ammount', models.CharField(max_length=255, null=True, verbose_name='trip_ammount')),
                ('trip_cart_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('trip_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='shangkai_app.my_trips')),
            ],
            options={
                'verbose_name': 'Trip Booking',
                'verbose_name_plural': 'Trip Booking',
            },
        ),
        migrations.CreateModel(
            name='User_Trip_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('no_guests', models.CharField(max_length=255, null=True, verbose_name='no_guests')),
                ('trip_cart_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('trip_id', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='shangkai_app.my_trips')),
            ],
            options={
                'verbose_name': 'Trip Carts',
                'verbose_name_plural': 'Trip Carts',
            },
        ),
        migrations.CreateModel(
            name='User_Trips_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('payment_id', models.CharField(max_length=255, null=True, verbose_name='payment_id')),
                ('payment_status', models.CharField(default='0', max_length=255, null=True, verbose_name='status')),
                ('trip_booking', models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user_trip_booking')),
            ],
            options={
                'verbose_name': 'User Trips Payments',
                'verbose_name_plural': 'User Trips Payments',
            },
        ),
        migrations.RenameModel(
            old_name='Account_Details',
            new_name='User_Account_Details',
        ),
        migrations.RemoveField(
            model_name='hotel_booking',
            name='hotel_id',
        ),
        migrations.RemoveField(
            model_name='hotel_booking',
            name='room_id',
        ),
        migrations.RemoveField(
            model_name='hotel_booking',
            name='user',
        ),
        migrations.AddField(
            model_name='normal_userreg',
            name='otp',
            field=models.CharField(max_length=255, null=True, verbose_name='otp'),
        ),
        migrations.AlterField(
            model_name='normal_userreg',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='normal_userreg',
            name='image',
            field=models.FileField(default='0', max_length=255, null=True, upload_to='', verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='Cab_Booking',
        ),
        migrations.DeleteModel(
            name='Hotel_Booking',
        ),
        migrations.AddField(
            model_name='user_trips_payment',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_trip_cart',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_trip_booking',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_hotspots_cart',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_hotspots_bookings',
            name='cart_id',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user_hotspots_cart'),
        ),
        migrations.AddField(
            model_name='user_hotspots_bookings',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_hotel_payment',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_hotel_cart',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_hotel_booking',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_guide_booking',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_cab_payment',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_cab_cart',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
        migrations.AddField(
            model_name='user_cab_booking',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
    ]
