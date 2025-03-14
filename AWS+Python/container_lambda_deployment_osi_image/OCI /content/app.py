# app.py
import pandas as pd

def lambda_handler(event, context):
    try:
        items = event.get('items', [])

        # Convert input items to DataFrame
        df = pd.DataFrame(items)

        # Simple data transformation: capitalize names, ensure prices are floats
        df['name'] = df['name'].str.capitalize()
        df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)

        # Calculate summary statistics
        total_price = df['price'].sum()
        average_price = df['price'].mean()

        # Convert DataFrame back to dict
        transformed_items = df.to_dict(orient='records')

        return {
            'statusCode': 200,
            'total_price': total_price,
            'average_price': average_price,
            'transformed_items': transformed_items
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'error': str(e),
            'message': 'Invalid input format. Expecting {"items":[{"name":"str", "price":number}, ...]}'
        }
