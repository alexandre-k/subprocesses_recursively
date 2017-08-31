import System.Process
import System.IO


main :: IO()
main = do
  let cmd = "mplayer"
      args = ["-fs", "muay_thai.mp4"]
  (_, Just hout, _, _) <- createProcess (proc cmd args) { std_out = CreatePipe }
  result <- hGetContents hout
  putStrLn result
  main
