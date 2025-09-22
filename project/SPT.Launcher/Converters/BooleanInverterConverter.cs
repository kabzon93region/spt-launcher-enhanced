using Avalonia.Data.Converters;
using System;
using System.Globalization;

namespace SPT.Launcher.Converters
{
    public class BooleanInverterConverter : IValueConverter
    {
        public static readonly BooleanInverterConverter Instance = new BooleanInverterConverter();

        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is bool boolValue)
            {
                return !boolValue;
            }
            return false;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is bool boolValue)
            {
                return !boolValue;
            }
            return false;
        }
    }
}
