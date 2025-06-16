import pandas as pd
from io import BytesIO
import xlsxwriter


def export_to_excel(products):
    """导出产品数据到Excel"""
    df = pd.DataFrame([{
        'ID': p.id,
        '系列': p.series,
        'SPU': p.spu,
        'SKU': p.sku,
        '文件受控': p.file_control,
        '标准化落地': p.standardization
    } for p in products])

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='产品数据', index=False)

        # 获取工作簿和工作表对象
        workbook = writer.book
        worksheet = writer.sheets['产品数据']

        # 设置格式
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'fg_color': '#D7E4BC',
            'border': 1
        })

        # 应用格式到标题行
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

        # 自动调整列宽
        for i, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(i, i, max_len)

    output.seek(0)
    return output
