# Australian ADI Deposits Bar Chart Race

An animated bar chart race visualisation showing the evolution of Australia's top 4 Authorised Deposit-taking Institutions (ADIs) deposits over time. Created using Python and the bar_chart_race library.

## 🎥 Preview



https://github.com/user-attachments/assets/0922c59f-8a4d-495a-903c-ab0535fe62d6



## 🛠️ Technologies Used

- Python 3.x
- pandas
- bar_chart_race
- matplotlib

## 📋 Prerequisites

- Python 3.x installed
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/adi-deposits-race.git
cd adi-deposits-race
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 📊 Data

The project uses data from the Australian Prudential Regulation Authority (APRA) on ADI deposits. The data is stored in `FULLADIDEPOSIT.csv`.

## 🚀 Usage

Run the script to generate the bar chart race animation:

```bash
python create_race.py
```

This will create a video file named `top_4_ADI.mp4` in the current directory.

## ⚙️ Configuration

You can modify the following parameters in `create_race.py`:
- `n`: Number of frames to sample (default: 2)
- `total_desired_frames`: Total number of frames in the output video (default: 1800 for 30 seconds at 60fps)
- `period_length`: Duration of each period in milliseconds (default: 500)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/adi-deposits-race/issues).

## 👤 Author

David Ma

## 🙏 Acknowledgments

- Data source: APRA
- Inspired by bar chart race visualisations
- Created with the assistance of GenAI 
