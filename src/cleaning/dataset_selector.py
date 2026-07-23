class DatasetSelector:

    def __init__(

        self,

        reject_blurry=True,

        reject_duplicates=True,

        reject_overexposed=False,

        reject_underexposed=False

    ):

        self.reject_blurry = reject_blurry

        self.reject_duplicates = reject_duplicates

        self.reject_overexposed = reject_overexposed

        self.reject_underexposed = reject_underexposed

    def should_keep(self,row):

        if self.reject_blurry:

            if row["blur_status"]=="rejected":

                return False

        if self.reject_duplicates:

            if row["keep_image"]==False:

                return False

        if self.reject_overexposed:

            if row["exposure_status"]=="overexposed":

                return False

        if self.reject_underexposed:

            if row["exposure_status"]=="underexposed":

                return False

        return True