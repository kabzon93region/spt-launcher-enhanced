using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Input;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Layout;
using Avalonia.Markup.Xaml;
using SPT.Launcher.Controllers;
using System.Reactive;
using ReactiveUI;
using SPT.Launcher.Models.Fika;
using SPT.Launcher.Helpers;

namespace SPT.Launcher.CustomControls;

public partial class OnlinePlayers : UserControl
{
    // Dictionary and activity strings as class fields for reuse
    private string[] GetActivityStrings()
    {
        return new string[] 
        { 
            LocalizationProvider.Instance.activity_in_menu,
            LocalizationProvider.Instance.activity_in_raid,
            LocalizationProvider.Instance.activity_in_stash,
            LocalizationProvider.Instance.activity_in_hideout,
            LocalizationProvider.Instance.activity_is_trading
        };
    }

    private Dictionary<string, string> GetMaps()
    {
        return new Dictionary<string, string>
        {
            { "factory4_day", LocalizationProvider.Instance.map_factory4_day },
            { "factory4_night", LocalizationProvider.Instance.map_factory4_night },
            { "bigmap", LocalizationProvider.Instance.map_bigmap },
            { "Interchange", LocalizationProvider.Instance.map_interchange },
            { "RezervBase", LocalizationProvider.Instance.map_rezervbase },
            { "Woods", LocalizationProvider.Instance.map_woods },
            { "Shoreline", LocalizationProvider.Instance.map_shoreline },
            { "TarkovStreets", LocalizationProvider.Instance.map_tarkovstreets },
            { "Sandbox", LocalizationProvider.Instance.map_sandbox },
            { "laboratory", LocalizationProvider.Instance.map_laboratory },
            { "Lighthouse", LocalizationProvider.Instance.map_lighthouse }
        };
    }

    public OnlinePlayers()
    {
        InitializeComponent();

        // Create a default command that updates the UI
        UpdateOnlinePlayersCommand = ReactiveCommand.CreateFromTask(async () =>
        {
            // This will update the UI, but we want parent ViewModel to also 
            // handle this and update PlayersOnline count
            await UpdatePlayersList();
        });

        // Initial load of players
        UpdatePlayersList();
    }

    public static readonly StyledProperty<ICommand> UpdateOnlinePlayersCommandProperty = AvaloniaProperty.Register<OnlinePlayers, ICommand>(nameof(UpdateOnlinePlayersCommand));

    public ICommand UpdateOnlinePlayersCommand
    {
        get => GetValue(UpdateOnlinePlayersCommandProperty);
        set => SetValue(UpdateOnlinePlayersCommandProperty, value);
    }

    // Modified to accept players parameter to avoid duplicate API calls
    public Task UpdatePlayersList(FikaPlayer[]? players = null)
    {
        // Clear the existing list first
        var stackPanel = this.FindControl<StackPanel>("onlinePlayersList");
        if (stackPanel != null)
        {
            stackPanel.Children.Clear();
        }

        // Use provided players or fetch if none provided
        if (players == null)
        {
            players = FikaController.GetOnlinePlayers();
        }

        foreach (var player in players)
        {
            if (player != null)
            {
                var border = new Border
                {
                    BorderBrush = Avalonia.Media.Brushes.Black,
                    BorderThickness = new Thickness(1),
                    Margin = new Thickness(5),
                    Padding = new Thickness(10)
                };

                var horizontalStack = new StackPanel { Orientation = Orientation.Horizontal };

                var verticalStack1 = new StackPanel { Orientation = Orientation.Vertical };
                verticalStack1.Children.Add(new Label { Content = LocalizationProvider.Instance.player_name });
                verticalStack1.Children.Add(new Label { Content = LocalizationProvider.Instance.current_activity });

                var activityStrings = GetActivityStrings();
                var maps = GetMaps();
                
                string activityString = String.Format("{0}", activityStrings[player.activity]);

                if (player.activity == 1)
                    activityString = String.Format(LocalizationProvider.Instance.activity_raid_format,
                        activityStrings[player.activity],
                        maps.ContainsKey(player.RaidInformation.location) ? maps[player.RaidInformation.location] : player.RaidInformation.location,
                        player.RaidInformation.side,
                        ((Int32)(DateTime.Now.Subtract(new DateTime(1970, 1, 1))).TotalSeconds - player.activityStartedTimeStamp) / 60);

                var verticalStack2 = new StackPanel { Orientation = Orientation.Vertical };
                verticalStack2.Children.Add(new Label { Content = player.nickname });
                verticalStack2.Children.Add(new Label { Content = activityString });

                horizontalStack.Children.Add(verticalStack1);
                horizontalStack.Children.Add(verticalStack2);

                border.Child = horizontalStack;

                stackPanel?.Children.Add(border);
            }
        }

        return Task.CompletedTask;
    }

    private void InitializeComponent()
    {
        AvaloniaXamlLoader.Load(this);
    }
}
