from .user import UserViewSet
from .category import CategoryViewSet
from .discount_coupon import DiscountCouponViewSet
from .service import ServiceViewSet
from .room import RoomViewSet
from .booking import BookingViewSet
from .room_availability import RoomAvailabilityViewSet
from .booking_service import BookingServiceViewSet
from .cancellation import CancellationViewSet
from .payment import PaymentViewSet
from .feedback import FeedbackViewSet
from .booking_room import BookingRoomViewSet
from .room_photo import RoomPhotoViewSet
from .custom.check_discount_code import CheckDiscountCouponView
from .custom.password_reset_confirmation import PasswordResetConfirmView
from .custom.password_reset_request import PasswordResetRequestView
from .lodge_photo import LodgePhotoViewSet
from .lodge import LodgeViewSet, LodgePolicyViewSet, LodgePaymentMethodViewSet, LodgeAmenityViewSet