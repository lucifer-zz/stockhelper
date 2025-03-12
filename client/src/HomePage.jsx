import { Row, Col, Card, Statistic } from 'antd';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ReactECharts from 'echarts-for-react';

export default function HomePage() {
  const [turnover, setTurnover] = useState(0);
  const [marginBalance, setMarginBalance] = useState(0);
  const [marginChange, setMarginChange] = useState(0);
  const [sectors, setSectors] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/market-data');
        setTurnover(response.data.turnover);
        setMarginBalance(response.data.marginBalance);
        setMarginChange(response.data.marginChange);
        setSectors(response.data.hotSectors);
      } catch (error) {
        console.error('数据获取失败:', error);
      }
    };
    
    fetchData();
    const timer = setInterval(fetchData, 10000);
    return () => clearInterval(timer);
  }, []);

  const chartOptions = {
    tooltip: {
      trigger: 'item'
    },
    series: [{
      type: 'pie',
      radius: '60%',
      data: sectors.slice(0, 5).map(sector => ({
        value: sector.value,
        name: sector.name
      })),
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }]
  };

  return (
    <div style={{ padding: 24 }}>
      <Row gutter={[24, 24]}>
        <Col span={8}>
          <Card title="A股成交额">
            <Statistic
              valueStyle={{ fontSize: 24 }}
              value={turnover}
              suffix="亿元"
            />
          </Card>
        </Col>

        <Col span={8}>
          <Card title="融资融券余额">
            <Statistic
              valueStyle={{ fontSize: 24 }}
              value={marginBalance}
              suffix="亿元"
            />
            <div style={{ marginTop: 12 }}>
              较前日：{marginChange >= 0 ? '+' : ''}{marginChange} 亿元
            </div>
          </Card>
        </Col>

        <Col span={8}>
          <Card title="热门板块">
            <div style={{ height: 300 }}>
              <ReactECharts option={chartOptions} style={{ height: 280 }} />
            </div>
          </Card>
        </Col>
      </Row>
    </div>
  );
}