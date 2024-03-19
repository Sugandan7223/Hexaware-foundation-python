from abc import ABC, abstractmethod


class TrackingNumberNotFoundException(Exception):
    pass


class InvalidEmployeeIdException(Exception):
    pass


class ICourierUserService(ABC):
    @abstractmethod
    def placeOrder(self, courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass


class ICourierAdminService(ABC):
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        pass

