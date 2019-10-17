#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))


def train():
    pass


def test():
    pass


def cli():
    """
    Define and parse command line arguments
    """

    prog_descrip = 'Auto-motion fmriprep'

    parser = argparse.ArgumentParser(description=prog_descrip,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b', '--bids', metavar='BIDS Dir', action='store', required=True,
                        help='absolute path to your top level bids folder.',
                        dest='bids_dir'
                        )
    parser.add_argument('-s', '--study', metavar='Study Name', action='store', type=str, required=True,
                        help='Study name.',
                        dest='study'
                        )
    parser.add_argument('-l', '--level', action='store', required=True, type=str,
                        help='Level of the classification that will be performed.',
                        choices=['train', 'test'],
                        dest='level'
                        )
    parser.add_argument('-ne', '--no-euc', action='store_true', required=False, default=False,
                        help=('Do NOT use euclidean distance. Uses RAW realignment \
                            parameters instead. This arg SUPPRESSES euclidean distance \
                            for realignment parameters.'),
                        dest='noeuc'
                        )
    parser.add_argument('-nr', '--no-rp', action='store_true', required=False, default=False,
                        help='No rp_txt files. This arg SUPPRESSES file write.',
                        dest='norp'
                        )
    parser.add_argument('-np', '--no-plot', action='store_true', required=False, default=False,
                        help='No plots created. This arg SUPPRESSES plot creation.',
                        dest='noplot'
                        )
    parser.add_argument('-f', '--fig-format', metavar='Fig File Format', action='store', type=str,
                        required=False, default='.png',
                        help='file format for plot.',
                        dest='f_format'
                        )
    parser.add_argument('-h', '--fig-height', metavar='Fig Height', action='store', type=str,
                        required=False, default='5.5',
                        help='plot height in inches.',
                        dest='f_height'
                        )
    parser.add_argument('-w', '--fig-width', metavar='Fig Width', action='store', type=str,
                        required=False, default='7.0',
                        help='plot width in inches.',
                        dest='f_width'
                        )
    parser.add_argument('-dpi', '--fig-dpi', metavar='Fig DPI', action='store', type=str,
                        required=False, default='250',
                        help='plot resolution in dots per inch.',
                        dest='f_dpi'
                        )
    parser.add_argument('-c', '--fig-csf', action='store_true', 
                        required=False, default=False,
                        help=('Print CSF motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_csf'
                        )
    parser.add_argument('-wm', '--fig-wm', action='store_true',
                        required=False, default=False,
                        help=('Print white matter motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_wm'
                        )
    parser.add_argument('-g', '--fig-gs', action='store_true', 
                        required=False, default=True,
                        help=('Print global signal motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_gs'
                        )
    parser.add_argument('-dv', '--fig-dvars', action='store_true', 
                        required=False, default=False,
                        help=('Print non-standardized DVARS motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_dvars'
                        )
    parser.add_argument('-sdv', '--fig-sdvars', action='store_true', 
                        required=False, default=True,
                        help=('Print standardized DVARS motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_sdvars'
                        )
    parser.add_argument('-vsdv', '--fig-vsdvars', action='store_true', 
                        required=False, default=False,
                        help=('Print voxel-wise standardized DVARS motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_vsdvars'
                        )
    parser.add_argument('-fd', '--fig-fd', action='store_true', 
                        required=False, default=True,
                        help=('Print framewise displacement motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_fd'
                        )
    parser.add_argument('-xt', '--fig-xtrans', action='store_true', 
                        required=False, default=False,
                        help=('Print x translation motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_xtrans'
                        )
    parser.add_argument('-yt', '--fig-ytrans', action='store_true', 
                        required=False, default=False,
                        help=('Print y translation motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_ytrans'
                        )
    parser.add_argument('-zt', '--fig-ztrans', action='store_true', 
                        required=False, default=False,
                        help=('Print z translation motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_ztrans'
                        )
    parser.add_argument('-xr', '--fig-xrot', action='store_true', 
                        required=False, default=False,
                        help=('Print x rotation motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_xrot'
                        )
    parser.add_argument('-yr', '--fig-yrot', action='store_true', 
                        required=False, default=False,
                        help=('Print y rotation motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_yrot'
                        )
    parser.add_argument('-zr', '--fig-zrot', action='store_true', 
                        required=False, default=False,
                        help=('Print z rotation motion indicator in plot. If you select \
                            more than three total, you may need to adjust the \
                            figure dimensions'),
                        dest='f_zrot'
                        )

    args = parser.parse_args()

    return args


def pngmaker():
    # #------------------------------------------------------
    # # write plots
    # #------------------------------------------------------
    # # plot indicators values as a function of time for the motion indicators specified in config.R
    # if (noPlot == FALSE) {
    # message(sprintf('--------Writing plots to %s--------', plotDir))
    # # create the plot directory if it does not exist
    # if (!file.exists(plotDir)) {
    #     message(paste0(plotDir, ' does not exist. Creating it now.'))
    #     dir.create(plotDir, recursive = TRUE)
    # }
    
    # # save the plots
    # plots_written = dataset %>% 
    #     mutate(label = ifelse(grepl(1, trash), as.character(volume), ''),
    #         code = ifelse(trash == 1, 'trash', NA)) %>%
    #     gather(indicator, value, figIndicators) %>%
    #     group_by(subjectID, wave, task, run) %>%
    #     do({
    #     plot = ggplot(., aes(x = volume, y = value)) +
    #         geom_line(data = filter(., subjectID == .$subjectID[[1]] & wave == .$wave[[1]] & task == .$task[[1]] & run == .$run[[1]]), size = .25) +
    #         geom_point(data = subset(filter(., subjectID == .$subjectID[[1]] & wave == .$wave[[1]] & task == .$task[[1]] & run == .$run[[1]]), !is.na(code)), aes(color = code), size = 4) +
    #         geom_text(data = filter(., subjectID == .$subjectID[[1]] & wave == .$wave[[1]] & task == .$task[[1]] & run == .$run[[1]]), aes(label = label), size = 2) +
    #         facet_grid(indicator ~ ., scales = 'free') +
    #         scale_color_manual(values = "#E4B80E") +
    #         labs(title = paste0(.$subjectID[[1]], "  ", .$wave[[1]], "  ", .$task[[1]], "  ", .$run[[1]]),
    #         y = "value\n",
    #         x = "\nvolume") +
    #         theme_minimal(base_size = 10) +
    #         theme(legend.position = "none")
    #     ggsave(plot, file = file.path(plotDir, paste0(.$subjectID[[1]], '_', .$wave[[1]], '_', .$task[[1]], '_', .$run[[1]], figFormat)), height = figHeight, width = figWidth, dpi = figDPI)
    #     data.frame()
    #     })
    # }

    pass


def txtmaker():
    # #------------------------------------------------------
    # # write rps
    # #------------------------------------------------------
    # # select relevant data
    # rps = dataset %>%
    # select(subjectID, wave, task, run, volume, X, Y, Z, RotX, RotY, RotZ, trash)

    # # write files
    # if (noRP == FALSE) {
    # message(sprintf('--------Writing text files to %s--------', rpDir))
    # if (noEuclidean == FALSE) {
    #     message('Transforming realignment parameters to Euclidean distance')
    #     # ouput Euclidean distance and it's derivative rather than the original realignment parameters
        
    #     # define function to calculate Euclidean distance (i.e. the L2 norm)
    #     l2norm3ddf = function(a,b,c){
    #     aDF = data.frame(a,b,c)
    #     apply(aDF, 1, function(vect) norm(matrix(vect), 'f'))
    #     }
        
    #     # For the radian to arc-length conversion, remember: "An angle of 1 radian 
    #     # refers to a central angle whose subtending arc is equal in length to the 
    #     # radius." http://www.themathpage.com/aTrig/arc-length.htm
    #     # If we multiply the radian output of the realignment parameters by the average 
    #     # head radius of 50mm, we get a rotational displacement from the origin at the 
    #     # outside of an average skull.
    #     rps = rps %>%
    #     group_by(subjectID, wave, task, run) %>%
    #     mutate(RotX = 50*RotX,
    #             RotY = 50*RotY,
    #             RotZ = 50*RotZ,
    #             trans = l2norm3ddf(X, Y, Z),
    #             rot = l2norm3ddf(RotX, RotY, RotZ),
    #             deriv.trans = c(0, diff(trans)),
    #             deriv.rot = c(0, diff(rot))) %>%
    #     select(subjectID, wave, task, run, volume, trans, rot, deriv.trans, deriv.rot, trash)
        
    # }
    
    # # create the rp directory if it does not exist
    # if (!file.exists(rpDir)) {
    #     message(paste0(rpDir, ' does not exist. Creating it now.'))
    #     dir.create(rpDir, recursive = TRUE)
    # }
    
    # # write the files
    # rp_files_written = rps %>%
    #     arrange(subjectID, wave, task, run, volume) %>%
    #     group_by(subjectID, wave, task, run) %>%
    #     do({
    #     fname = file.path(rpDir, paste('rp_', .$subjectID[[1]], '_', .$wave[[1]], '_', .$task[[1]], '_', .$run[[1]], '.txt', sep = ''))
    #     write.table(
    #         .[,-c(1:5)],
    #         fname,
    #         quote = F,
    #         sep = '   ',
    #         row.names = F,
    #         col.names = F)
    #     data.frame(rp_file_name = fname)
    #     })
    # }

    pass


def summarize(df):
    # #------------------------------------------------------
    # # summarize data and write csv files
    # #------------------------------------------------------
    # message(sprintf('--------Writing summaries to %s--------', summaryDir))

    # # summarize by task and run
    # summaryRun = dataset %>% 
    # group_by(subjectID, wave, task, run) %>% 
    # summarise(nVols = sum(trash, na.rm = T),
    #             percent = round((sum(trash, na.rm = T) / n()) * 100, 1))

    # # summarize by task
    # summaryTask = dataset %>% 
    # group_by(subjectID, wave, task) %>% 
    # summarise(nVols = sum(trash, na.rm = T),
    #             percent = round((sum(trash, na.rm = T) / n()) * 100, 1))

    # # print all trash volumes
    # summaryTrash = dataset %>%
    # filter(trash == 1) %>%
    # select(subjectID, wave, task, run, volume, trash)

    # # create the summary directory if it does not exist
    # if (!file.exists(summaryDir)) {
    # message(paste0(summaryDir, ' does not exist. Creating it now.'))
    # dir.create(summaryDir, recursive = TRUE)
    # }

    # # write files
    # write.csv(summaryRun, file.path(summaryDir, paste0(study, '_summaryRun.csv')), row.names = FALSE)
    # write.csv(summaryTask, file.path(summaryDir, paste0(study, '_summaryTask.csv')), row.names = FALSE)
    # write.csv(summaryTrash, file.path(summaryDir, paste0(study, '_trashVols.csv')), row.names = FALSE)

    pass


def main():
    args = cli()

    r_args = ['Rscript', 'auto_motion_fmriprep.R',
              os.path.join(args.bids_dir, 'derivatives', 'fmriprep'),
              os.path.join(args.bids_dir, 'derivatives', 'auto-motion', 'summary'),
              os.path.join(args.bids_dir, 'derivatives', 'auto-motion', 'rp_text'),
              os.path.join(args.bids_dir, 'derivatives', 'auto-motion', 'plots'),
              args.study,
              str(args.noeuc).upper(), str(args.norp).upper(), str(args.noplot).upper(),
              args.f_format, args.f_height, args.f_width, args.f_dpi,
              str(args.f_csf).upper(), str(args.f_wm).upper(), str(args.f_gs).upper(), str(args.f_dvars).upper(),
              str(args.f_sdvars).upper(), str(args.f_vsdvars).upper(), str(args.f_fd).upper(),
              str(args.f_xtrans).upper(), str(args.f_ytrans).upper(), str(args.f_ztrans).upper(),
              str(args.f_xrot).upper(), str(args.f_yrot).upper(), str(args.f_zrot).upper()]
    r_process = subprocess.run(r_args, capture_output=True)
    print(r_process.stdout)
    print(r_process.stderr)


if __name__ == "__main__":
    sys.exit(main())
