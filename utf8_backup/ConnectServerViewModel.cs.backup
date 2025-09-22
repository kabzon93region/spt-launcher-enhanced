using SPT.Launcher.Models.SPT;
using SPT.Launcher.Helpers;
using SPT.Launcher.Models.Launcher;
using ReactiveUI;
using Splat;
using System.Reactive.Disposables;
using System.Threading.Tasks;
using SPT.Launcher.Controllers;
using System.Threading;
using System;

namespace SPT.Launcher.ViewModels
{
    public class ConnectServerViewModel : ViewModelBase
    {
        private bool noAutoLogin = false;
        private CancellationTokenSource _cancellationTokenSource;

        public ConnectServerModel connectModel { get; set; } = new ConnectServerModel()
        {
            InfoText = LocalizationProvider.Instance.server_connecting
        };

        public ConnectServerViewModel(IScreen Host, bool NoAutoLogin = false) : base(Host)
        {
            noAutoLogin = NoAutoLogin;

            this.WhenActivated((CompositeDisposable disposables) =>
            {
                // Отменяем предыдущие попытки подключения
                _cancellationTokenSource?.Cancel();
                _cancellationTokenSource = new CancellationTokenSource();
                
                Task.Run(async () =>
                {
                   await ConnectServer(_cancellationTokenSource.Token);
                });
                
                // Отменяем токен при деактивации
                disposables.Add(Disposable.Create(() => _cancellationTokenSource?.Cancel()));
            });
        }

        public async Task ConnectServer(CancellationToken cancellationToken = default)
        {
            await ConnectServerWithRetry(cancellationToken);
        }

        private async Task ConnectServerWithRetry(CancellationToken cancellationToken = default)
        {
            LauncherSettingsProvider.Instance.AllowSettings = false;
            
            bool connected = false;
            int maxAttempts = LauncherSettingsProvider.Instance.EnableRetryConnection ? 
                LauncherSettingsProvider.Instance.RetryAttempts : 1;
            int delay = LauncherSettingsProvider.Instance.RetryDelay * 1000; // конвертируем в миллисекунды

            for (int i = 0; i < maxAttempts; i++)
            {
                // Проверяем отмену перед каждой попыткой
                if (cancellationToken.IsCancellationRequested)
                {
                    LogManager.Instance.Info("[ConnectServer] Подключение отменено пользователем");
                    return;
                }

                connectModel.InfoText = i == 0 ? 
                    LocalizationProvider.Instance.server_connecting : 
                    $"{LocalizationProvider.Instance.server_connecting} ({LocalizationProvider.Instance.connection_attempt} {i + 1} {LocalizationProvider.Instance.connection_attempt_of} {maxAttempts})";

                // Попытка загрузить сервер
                if (!await ServerManager.LoadDefaultServerAsync(LauncherSettingsProvider.Instance.Server.Url))
                {
                    LogManager.Instance.Warning($"[ConnectServer] Попытка {i + 1}: Не удалось загрузить сервер");
                    
                    // После первой неудачной попытки показываем кнопку "Настройки"
                    if (i == 0)
                    {
                        LauncherSettingsProvider.Instance.AllowSettings = true;
                    }
                    
                    if (i < maxAttempts - 1)
                    {
                        LogManager.Instance.Info($"[ConnectServer] Повтор через {delay / 1000} секунд...");
                        try
                        {
                            await Task.Delay(delay, cancellationToken);
                        }
                        catch (OperationCanceledException)
                        {
                            LogManager.Instance.Info("[ConnectServer] Задержка отменена пользователем");
                            return;
                        }
                        continue;
                    }
                    else
                    {
                        connectModel.ConnectionFailed = true;
                        connectModel.InfoText = string.Format(LocalizationProvider.Instance.server_unavailable_format_1,
                            LauncherSettingsProvider.Instance.Server.Name);
                        break;
                    }
                }

                // Попытка пинга сервера
                connected = ServerManager.PingServer();
                
                if (connected)
                {
                    LogManager.Instance.Info($"[ConnectServer] Успешное подключение с попытки {i + 1}");
                    break;
                }
                else
                {
                    LogManager.Instance.Warning($"[ConnectServer] Попытка {i + 1}: Сервер не отвечает на пинг");
                    
                    // После первой неудачной попытки показываем кнопку "Настройки"
                    if (i == 0)
                    {
                        LauncherSettingsProvider.Instance.AllowSettings = true;
                    }
                    
                    if (i < maxAttempts - 1)
                    {
                        LogManager.Instance.Info($"[ConnectServer] Повтор через {delay / 1000} секунд...");
                        try
                        {
                            await Task.Delay(delay, cancellationToken);
                        }
                        catch (OperationCanceledException)
                        {
                            LogManager.Instance.Info("[ConnectServer] Задержка отменена пользователем");
                            return;
                        }
                    }
                }
            }

            connectModel.ConnectionFailed = !connected;

            if (connected)
            {
                connectModel.InfoText = LocalizationProvider.Instance.ok;
                
                SPTVersion version = Locator.Current.GetService<SPTVersion>("sptversion");
                version.ParseVersionInfo(ServerManager.GetVersion());
                
                LogManager.Instance.Info($"Connected to server: {ServerManager.SelectedServer.backendUrl} - SPT MatchingVersion: {version}");

                NavigateTo(new LoginViewModel(HostScreen, noAutoLogin));
            }
            else
            {
                connectModel.InfoText = string.Format(LocalizationProvider.Instance.server_unavailable_format_1, 
                    LauncherSettingsProvider.Instance.Server.Name);
                LogManager.Instance.Warning($"[ConnectServer] Все {maxAttempts} попыток подключения исчерпаны");
            }
            
            // Убеждаемся, что кнопка "Настройки" всегда доступна в конце
            LauncherSettingsProvider.Instance.AllowSettings = true;
        }

        public void RetryCommand()
        {
            connectModel.InfoText = LocalizationProvider.Instance.server_connecting;
            connectModel.ConnectionFailed = false;

            // Отменяем предыдущие попытки подключения
            _cancellationTokenSource?.Cancel();
            _cancellationTokenSource = new CancellationTokenSource();

            Task.Run(async () =>
            {
                await ConnectServerWithRetry(_cancellationTokenSource.Token);
            });
        }
    }
}
