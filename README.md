# Car_Rental_api_using_django_restframework
Authentication:
I have implemented login and register feature in this api .
Jwt authentication system has been used here.

Owner:
owner can retirve ,add , update and delete vehicle details add by him/her.
owner can see only those vehicles details which are add by him.
owner can cancle or approve booking requests sent by user.
owner can check all his rent history.

Renter: 
renter can see every vehicles information that are present in car table
renter can send a vehicle booking request to owner.
a renter can send request for multiple vehicle.
renter can check all his rent history.

models used:
custom user model
cars
booking request
login logs

general information for both owner and renter:
i have cretaed two viewsets CarView and BookingRequestView in views.py which can handle requests for both owner and renter
i have created custom permissions to handle owner and renter requests
i have created signals logic to maintain login data of user(owner/renter)

modificication that can be done furhter:
currently i am saving pending requests and confirm/cancle requests in same table , we can seprate it and make confirm/cancle requests unchangable in order 
to maintain records.
a dynamic folder directory to store images in more organized manner , currently i am adding all uploaded images in cars folder.
