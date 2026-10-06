import pandas as pd


class VendorFileTool:

    def process_file(self, file_path):

        data = pd.read_csv(file_path)

        required_columns = [
            "vendor_id",
            "product_id",
            "product_name",
            "price",
            "quantity"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in data.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing columns: {missing_columns}"
            )

        invalid_rows = []

        for index, row in data.iterrows():

            errors = []

            if row["price"] <= 0:
                errors.append("Price must be greater than 0")

            if row["quantity"] < 0:
                errors.append("Quantity cannot be negative")

            if not row["product_id"]:
                errors.append("Product ID is required")

            if errors:
                invalid_rows.append({
                    "row_number": index + 2,
                    "product_id": row["product_id"],
                    "product_name": row["product_name"],
                    "errors": errors
                })

        return {
            "total_rows": len(data),
            "valid_rows": len(data) - len(invalid_rows),
            "invalid_rows": invalid_rows
        }