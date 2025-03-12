import akshare as ak
import datetime
from pprint import pprint

try:
    # 生成测试日期
    test_date = datetime.datetime.now() - datetime.timedelta(days=1)
    date_str = test_date.strftime('%Y%m%d')
    print(f'测试日期参数: {date_str}')

    # 调用接口
    df = ak.stock_sse_deal_daily(date=date_str)

    # 打印完整响应信息
    print('\n=== 接口返回字段 ===')
    pprint(df.columns.tolist())
    
    print('\n=== 前3条数据样例 ===')
    pprint(df.head(3).to_dict())
    
    print('\n=== 数据类型 ===')
    pprint(df.dtypes.to_dict())
    
    # 深度解析数据结构
    print('\n=== 字段值分布 ===')
    print('单日情况字段取值:', df['单日情况'].unique().tolist())
    
    if '成交金额' in df['单日情况'].values:
        turnover_row = df[df['单日情况'] == '成交金额']
        print('\n成交金额数据:\n', turnover_row.to_markdown())
    else:
        print('\n警告: 未找到成交金额字段')
        print('可用指标:', df['单日情况'].unique())

    # 添加多日期测试
    for days_back in range(1, 4):
        test_date = datetime.datetime.now() - datetime.timedelta(days=days_back)
        while test_date.weekday() >= 5:
            test_date -= datetime.timedelta(days=1)
        date_str = test_date.strftime('%Y%m%d')
        print(f'\n=== 测试历史日期 {date_str} ===')
        try:
            df = ak.stock_sse_deal_daily(date=date_str)
            print('最新数据日期:', df.iloc[0]['日期'] if '日期' in df.columns else '无日期字段')
        except Exception as e:
            print(f'日期 {date_str} 请求失败:', str(e))
    # 补充外层try的except块
    
except Exception as e:
    print(f'测试发生异常: {str(e)}')