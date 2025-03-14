from datetime import datetime, timedelta

class Booking:
    def __init__(
        self,
        id,
        start_date,
        end_date,
        user_id,
        space_id,
        subtotal=0,
        service_fee=0,
        total=0,
        approved=False,
    ):
        self.id = id
        self.user_id = user_id
        self.space_id = space_id
        self.requested_dates_list = self.create_dates_requested_list(
            start_date, end_date
        )
        self.subtotal = subtotal
        self.service_fee = service_fee
        self.total = total
        self.approved = approved
        self.nights = len(self.requested_dates_list) - 1

    def __repr__(self):
        return (
            f"Booking(ID: {self.id}, {self.requested_dates_list} "
            f"Customer User ID: {self.user_id}, Space ID: {self.space_id}, "
            f"Total: {self.total})"
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def create_dates_requested_list(self, start_date, end_date):
        dates_requested_list = []
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        current_date = start_date
        while current_date <= end_date:
            dates_requested_list.append(str(current_date.date()))
            current_date += timedelta(days=1)
        return dates_requested_list

    def mark_as_approved(self):
        self.approved = True

    # def deny_booking(self):
        
    #     self.approved = False


    @classmethod
    def from_database(
        cls,
        id,
        user_id,
        space_id,
        requested_dates_list,
        subtotal=0,
        service_fee=0,
        total=0,
        approved=False,
    ):
        # Create a new instance
        instance = cls.__new__(cls)

        # Set attributes directly
        instance.id = id
        instance.requested_dates_list = requested_dates_list[1:-1].split(", ")
        instance.user_id = user_id
        instance.space_id = space_id
        instance.subtotal = subtotal
        instance.service_fee = service_fee
        instance.total = total
        instance.approved = approved
        instance.nights = len(instance.requested_dates_list) - 1

        return instance
